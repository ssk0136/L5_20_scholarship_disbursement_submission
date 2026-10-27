"""Manage scholarship awards and disbursements."""

import sqlite3


def create_connection():
    """Create an in-memory scholarship ledger."""
    database = sqlite3.connect(":memory:")
    database.execute(
        "CREATE TABLE awards ("
        "id INTEGER PRIMARY KEY, "
        "student TEXT, "
        "scheme TEXT, "
        "amount INTEGER, "
        "disbursed INTEGER)"
    )
    return database


def grant(database, student, scheme, amount, audit=None):
    """Record a scholarship award and update the supplied audit list."""
    if audit is None:
        audit = []
    database.execute(
        "INSERT INTO awards (student, scheme, amount, disbursed) "
        "VALUES (?, ?, ?, 0)",
        (student, scheme, amount),
    )
    audit.append(student)
    return audit


def disburse(database, award_id):
    """Disburse an unpaid award once, if it exists."""
    row = database.execute(
        "SELECT amount, disbursed FROM awards WHERE id = ?",
        (award_id,),
    ).fetchone()
    if row is None or row[1]:
        return None
    database.execute(
        "UPDATE awards SET disbursed = 1 WHERE id = ?",
        (award_id,),
    )
    return row[0]


def archive(database):
    """Save any pending ledger changes without invoking a shell."""
    database.commit()
    print("Archiving awards")


def by_scheme_count(database, scheme):
    """Count awards for a scholarship scheme."""
    if scheme is None:
        return 0
    return database.execute(
        "SELECT COUNT(*) FROM awards WHERE scheme = ?",
        (scheme,),
    ).fetchone()[0]


def main():
    """Run the scholarship ledger demonstration."""
    with create_connection() as database:
        grant(database, "Ishaan", "Merit", 50000)
        grant(database, "Divya", "Need-based", 75000)
        paid = disburse(database, 1)
        missing = disburse(database, 9)
        print(paid, missing)
        print(by_scheme_count(database, "Merit"), paid or 0)
        archive(database)


if __name__ == "__main__":
    main()

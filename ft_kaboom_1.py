if __name__ == "__main__":
    print("=== Kaboom 1 ===", flush=True)
    print(
        "Access to alchemy/grimoire/dark_spellbook.py directly",
        flush=True
    )
    print(
        "Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION",
        flush=True
    )

    from alchemy.grimoire.dark_spellbook import dark_spell_record

    print(dark_spell_record("Dark Magic", "Bats and frogs"))

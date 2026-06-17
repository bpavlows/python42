def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda a: a['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda m: m['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda s: f"* {s} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    if not mages:
        return {'max_power': 0, 'min_power': 0, 'avg_power': 0.0}

    max_p = max(mages, key=lambda x: x['power'])['power']
    min_p = min(mages, key=lambda x: x['power'])['power']
    avg_p = sum(map(lambda x: x['power'], mages)) / len(mages)

    return {
        'max_power': max_p,
        'min_power': min_p,
        'avg_power': round(avg_p, 2)
    }


def main() -> None:
    artifacts = [
        {'name': 'Crystal Orb', 'power': 85, 'type': 'magic'},
        {'name': 'Fire Staff', 'power': 92, 'type': 'fire'},
        {'name': 'Shadow Cloak', 'power': 78, 'type': 'shadow'},
    ]
    mages = [
        {'name': 'Alex', 'power': 45, 'element': 'water'},
        {'name': 'Jordan', 'power': 80, 'element': 'fire'},
        {'name': 'Riley', 'power': 95, 'element': 'earth'},
        {'name': 'Sam', 'power': 30, 'element': 'air'}
    ]

    print()
    print("Testing artifact sorter...")
    sorted_arts = artifact_sorter(artifacts)
    first = sorted_arts[0]
    second = sorted_arts[1]
    print(
        f"{first['name']} ({first['power']} power)"
        f" comes before"
        f" {second['name']} ({second['power']} power)"
    )

    print()
    print("Testing spell transformer...")
    spells = ['fireball', 'heal', 'shield']
    transformed = spell_transformer(spells)
    print(' '.join(transformed))

    print()
    print("Testing power filter...")
    filtered = power_filter(mages, 75)
    print(f"Mages with power >= 75: {len(filtered)}")

    print()
    print("Testing mage stats...")
    stats = mage_stats(mages)
    print(
            f"Stats: max={stats['max_power']}, "
            f"min={stats['min_power']} and "
            f"avg={stats['avg_power']}."
    )
    print()


if __name__ == "__main__":
    main()

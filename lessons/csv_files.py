def column_vals(table: list[dict[str, str]], header: str) -> list[str]:
    """Returns table column values under a specific header."""
    result: list[str] = []
    #step through the table
    for row in table:
        #save every value under key "header"
        result.append[row[header]]
    return result

x: list[dict[str, str]] = [{"Comp": "110", "Bio": "100"}, {"Comp": "210", "Bio": "200"}]
column_vals(x, "Comp")

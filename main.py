import JSON_Parser
import validations

if __name__ == '__main__':
    data = JSON_Parser.load_json()
    graf, komps = JSON_Parser.load_components(data)
    JSON_Parser.load_edges(data, graf)
    # labels = graf.dfs(komps[10].id)
    validations.validate_bus_join(graf)
    validations.validate_calc_value_not_used(graf)
    print()
    # for komp in komps:
    #     print(komp)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

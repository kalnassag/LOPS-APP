from neo4j import GraphDatabase

URI = 'neo4j+s://e4f7116d.databases.neo4j.io'
AUTH = ("neo4j", "ifHkrzNq3YpJkY9La9EWU71XhTzsyu_K4KAU_0ewmlI")

with GraphDatabase.driver(URI, auth=AUTH) as driver:
    driver.verify_connectivity()
    print("Connection Established")

    # summary = driver.execute_query("""
    #     CREATE (a:Person {name: $name})
    #     CREATE (b:Person {name: $friendName})
    #     CREATE (a)-[:KNOWS]->(b)
    #     """,
    #     name="Alice", friendName = "David",
    #     # impersonated_user_= "rauxenfans@outlook.com",
    #     database_= "neo4j"
    #     ).summary
    # print("Created {nodes_created} nodes in {time} ms.".format(
    #     nodes_created=summary.counters.nodes_created,
    #     time=summary.result_available_after))

    # records, summary, keys = driver.execute_query("""
    #     MATCH (p1:Person)-[:KNOWS]->(p2:Person)
    #     RETURN p1.name AS name, p2.name
    #     """,
    #     database_="neo4j"
    # )
    #
    # for record in records:
    #     print(record.data())
    #
    # print("The query '{query}' returned {records_count} records in {time} ms.".format(
    #     query=summary.query, records_count=len(records),
    #     time = summary.result_available_after
    # ))

    # records, summary, keys = driver.execute_query("""
    #     match (p:Person {name: $name})
    #     SET p.age = $age
    #     """, name = "Alice", age=42,
    #     database_="neo4j",
    # )
    # print(f"Query counters: {summary.counters}.")

    records, summary, keys = driver.execute_query("""
        MATCH (alice:Person {name: $name})
        MATCH (david:Person {name: $friend})
        CREATE (alice)-[:KNOWS]->(david)
        """, name="Alice", friend="David",
                                                  database_="neo4j",
                                                  )
    print(f"Query counters: {summary.counters}.")

    # records, summary, keys = driver.execute_query("""
    #     MATCH (p:Person {name: $name})
    #     DETACH DELETE p
    #     """, name = "David",
    #     database_= "neo4j",
    # )
    # print(f"Query counters: {summary.counters}.")
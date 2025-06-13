Feature: Compare data between source and target databases

  Scenario: Validate that row counts and data match
    Given the source database "source.db"
    And the target database "target.db"
    When I compare the "customers" table
    Then the row counts should match
    And the data should match

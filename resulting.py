class Result:
    def __init__(self):
        self.result_file = open("results/result.txt", "w")

    def start_test(self, file_name):
        self.result_file.write("\n\nTesting of {} was started".format(file_name))

    def start_case(self, test_name):
        self.result_file.write("\n\nTest case '{}'".format(test_name))

    def add_pass(self, query, actual_result):
        self.result_file.write("\nPASS. Result is {0} as expected"
                               "\nQuery: {1}".format(actual_result, query))

    def add_fail(self, query, actual_result, expected_result):
        self.result_file.write("\nFAIL. Result is {0} \nbut expected    {1}"
                               "\nQuery: {2}".format(actual_result, expected_result, query))

    def finish_test(self):
        self.result_file.close()
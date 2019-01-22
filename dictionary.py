# comparing dictionary is empty checks

content_test_dict = {
    "test": True
}

empty_test_dict = {}

if not content_test_dict:
    print("Not Dict is Empt contenty")

if not empty_test_dict:
    print("Not Dict is Empty empty")


if content_test_dict is False:
    print("False Dict is Empty content")

if empty_test_dict is False:
    print("False Dict is Empty empty")

if content_test_dict is None:
    print("None Dict is Empty content")

if empty_test_dict is None:
    print("None Dict is Empty empty")


if content_test_dict is not None:
    print("Not None Dict is Empty content")

if empty_test_dict is not None:
    print("Not None Dict is Empty empty")


if bool(content_test_dict) is False:
    print("BoolFalse Dict is Empty content")

if bool(empty_test_dict) is False:
    print("BoolFalse Dict is Empty empty")

if len(content_test_dict.keys()) == 0:
    print("Len Dict is Empty content")

if len(empty_test_dict.keys()) == 0:
    print("Len Dict is Empty empty")
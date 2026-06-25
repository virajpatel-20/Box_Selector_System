# Test Output

## Test Environment

* Framework: Django 6.0.3
* Testing Framework: Django Test Framework
* Database: SQLite (Test Database)
* Operating System: Windows 11
* Python Version: 3.14.3

---

# Running the Tests

Execute the following command:

```bash
python manage.py test
```

---

# Test Results

```text
Found 4 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).

....

----------------------------------------------------------------------
Ran 4 tests in 0.013s

OK

Destroying test database for alias 'default'...
```

---

# Test Cases

## 1. Cheapest Eligible Box Selection

**Objective**

Verify that when multiple boxes satisfy the order requirements, the system recommends the lowest-cost box.

**Expected Result**

The lowest-cost eligible box is selected.

**Status**

PASS

---

## 2. No Suitable Box Available

**Objective**

Verify that the system correctly handles orders that cannot fit into any available shipping box.

**Expected Result**

The recommendation engine returns no suitable box.

**Status**

PASS

---

## 3. Weight Limit Validation

**Objective**

Ensure that boxes exceeding their maximum weight capacity are not recommended.

**Expected Result**

Boxes with insufficient weight capacity are rejected.

**Status**

PASS

---

## 4. Tie-Breaking Logic

**Objective**

Verify that when two boxes have the same shipping cost, the recommendation engine selects the smaller eligible box.

**Expected Result**

The smaller box is selected.

**Status**

PASS

---

# Manual Verification

The application was also manually tested using the web interface.

The following workflow was verified:

1. Open the application.
2. Enter product details.
3. Specify product quantity.
4. Submit the order.
5. Verify that an Order is created automatically.
6. Verify that the recommendation engine returns the appropriate shipping box.
7. Verify that the packaging cost is displayed correctly.

---

# Test Summary

| Test Case             | Status |
| --------------------- | ------ |
| Cheapest Eligible Box | PASS   |
| No Suitable Box       | PASS   |
| Weight Validation     | PASS   |
| Tie-Breaking Logic    | PASS   |

**Total Tests:** 4

**Passed:** 4

**Failed:** 0

**Overall Result:** ✅ All automated and manual tests passed successfully.

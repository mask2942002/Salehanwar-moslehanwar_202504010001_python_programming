## 1.1 Inputs

- Age
- Accompanied by an adult (True/False)
- Valid ticket (True/False)

## 1.2 Process

Check if:

(age >= 13 OR accompanied_by_adult) AND valid_ticket

## 1.3 Output

- Allow Entry = True
- Deny Entry = False

---

# 2. Design the Algorithm

## 2.1 Logic Diagram

```text
START
   |
   V
Input Age
Input Adult Status
Input Ticket Status
   |
   V
(Age >= 13 OR Adult Present)?
   |
  YES
   |
Valid Ticket?
   |
YES ------> ENTRY APPROVED
   |
NO
   |
ENTRY DENIED

If first condition = NO
   |
ENTRY DENIED
   |
END
```

---

## 2.2 Truth Table

| Age >= 13 | Adult | Ticket | Result |
|------------|--------|---------|---------|
| True | False | True | True |
| False | True | True | True |
| True | True | True | True |
| False | False | True | False |
| True | False | False | False |
| False | True | False | False |
| False | False | False | False |

---

## 2.3 Algorithm

1. Start
2. Input age
3. Input accompanied_by_adult
4. Input valid_ticket
5. Check if (age >= 13 OR accompanied_by_adult) AND valid_ticket
6. If true, allow entry
7. Otherwise deny entry
8. End

---

## 2.4 Pseudocode

text
BEGIN

INPUT age
INPUT accompanied_by_adult
INPUT valid_ticket

IF (age >= 13 OR accompanied_by_adult) AND valid_ticket THEN
    PRINT "Allow Entry"
ELSE
    PRINT "Deny Entry"
END IF

END


---

# 3. Evaluate Expression

## 3.1 Test Samples

| Age | Adult | Ticket | Result |
|------|--------|---------|---------|
| 15 | False | True | Allow Entry |
| 10 | True | True | Allow Entry |
| 10 | False | True | Deny Entry |
| 15 | False | False | Deny Entry |

### Python Code

python
age = 15
accompanied_by_adult = False
valid_ticket = True

can_enter = (age >= 13 or accompanied_by_adult) and valid_ticket

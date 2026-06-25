# AI_USAGE.md

# AI Usage Report

## 1. AI Tool Used

* ChatGPT (OpenAI)

The AI tool was used as a development assistant for debugging, code review, project improvements, testing, and documentation. The project implementation was completed manually and AI suggestions were reviewed before being incorporated.

---

# 2. Prompts Used

Below are the major prompts used during development.

---

### Recommendation Logic

* "Should I make a normal project or the whole warehouse optimization system?"
* "Created this in box_selector.py."
* "How to check the recommendation is correct or not?"
* "Why is it still recommending the Small Box?"
* "Review this recommend_box() function."

---

### Django Development

* "How to create a serializer?"
* "How to verify the URLs?"
* "How to connect all the URLs to one page for making a small UI?"

---

### User Interface

* "Should the order ID be generated automatically?"
* "Add all the box types in the database so that when the user adds the product it directly suggests the recommended box."
* "Add the quantity of product and according to the quantity also add the boxes."

---

### Debugging

* "Unknown command: seed_boxes."
* "Migration dependency error."
* "UnboundLocalError: quantity."

---

### Testing

* "Give the test cases."
* "How to test them step by step."
* "How to verify the recommendation is correct."

---

# 3. AI Suggestions Accepted

The following AI suggestions were accepted after manual review:

* Keeping business logic inside a separate `box_selector.py` service.
* Using Django REST Framework serializers.
* Creating REST API endpoints for Products, Boxes and Orders.
* Adding a Bootstrap-based interface.
* Creating a Django management command (`seed_boxes`) for inserting default shipping boxes.

---

# 4. AI Suggestions Modified or Rejected

### Data Migration

AI initially suggested inserting default boxes using Django migrations.
This approach caused migration dependency issues.
I replaced it with a custom Django management command (`python manage.py seed_boxes`).

---

### Manual Order ID

An early workflow required manually entering an Order ID.
I changed the workflow so that the application automatically creates an Order and immediately recommends a shipping box.

---

### Box Entry Form

An early version of the project allowed users to manually create shipping boxes through the interface.
I removed this functionality from the main workflow and instead preloaded standard shipping boxes using the management command.

---

### Automatically generating an Order 

An early version of the project didnot generated the order after product submission, so changed the output and add the function for automatically generating the order after product submission

---

### User Interface

Several UI suggestions were simplified to keep the project aligned with the assignment rather than expanding it into a complete warehouse management system.

---

# 5. Mistakes Found in AI Output

During development I identified and corrected several issues in AI-generated suggestions:

* Incorrect migration dependency configuration.
* Incorrect field names after model changes.
* Uninitialized variable (`quantity`) causing an `UnboundLocalError`.
* Initial recommendation workflow requiring manual Order ID input.
* Incorrect recommended boxs.
* HTML issues in the template.

These were manually debugged and corrected before being included in the project.

---

# 6. Verification

Every AI suggestion was verified manually before being accepted.

Verification included:

* Running Django migrations.
* Running the `seed_boxes` management command.
* Executing automated unit tests using:

```bash
python manage.py test
```

* Manually testing the web interface.
* Verifying box recommendations using different product dimensions, weights and quantities.
* Checking API endpoints.
* Reviewing the final repository structure before submission.

Only verified and working code was included in the final project.

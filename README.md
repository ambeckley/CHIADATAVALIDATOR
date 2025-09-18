# CHIADATAVALIDATOR

**CHIADATAVALIDATOR** is a very basic Python-based tool for validating raw CHIA healthcare data files and converting them into cleaned CSVs for database ingestion (e.g., PostgreSQL).

---

## Requirements

* **Python 3.11**
* Required packages can be installed via:

```bash
pip install pandas numpy
```


---

## Python Files and Their Purpose

| File                               | Purpose                                                |
| ---------------------------------- | ------------------------------------------------------ |
| `MedicalClaimValidator.py`         | Validates and transforms standard medical claim files. |
| `MedicalClaimValidator438.py`      | Same as above but for "438" format variant.            |
| `PharmacyClaimValidator.py`        | Validates standard pharmacy claim files.               |
| `PharmacyClaimValidator438.py`     | Validates pharmacy claim files in "438" variant.       |
| `MemberEligibilityValidator.py`    | Processes and validates eligibility/member data.       |
| `MemberEligibilityValidator438.py` | "438" version of eligibility validator.                |
| `ProductValidator.py`              | Validates product reference files.                     |
| `ProductValidator438.py`           | 438-format version of product file validator.          |
| `ProviderValidator.py`             | Validates provider information files.                  |
| `ProviderValidator438.py`          | 438-format version of provider validator.              |
| `OneZipValidator.py`               | Validates ZIP code data files.                         |
| `OneZipValidator438.py`            | 438-format ZIP code file validator.                    |

---

From the CSV files created you can import them into any other tool, such as SQL.

## Splitting CHIA Data Files on Linux

To split a large CHIA data file into smaller chunks (100,000 lines each), use the following command:

```bash
split -l 100000 -a 10 -d OrganizationNameMedicalClaim_Final.txt MedicalClaimPart1_
```

* `-l 100000`: splits every 100,000 lines
* `-a 10`: suffix length (creates files like `MedicalClaimPart1_0000000001`)
* `-d`: use numeric suffixes

The splitting is done due to ram limitations, the data is processed in chunks.

---

## Example SQL 

The SQL create commands for all of them are included.

---

## License

This project is licensed under the [Apache 2.0 License](LICENSE).

---


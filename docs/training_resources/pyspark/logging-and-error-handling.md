---
#hide table of contents whitespace
hide: toc
---

# Logging and error handling in PySpark

!!! Info
    See our documentation on [logging and error handling in Python][1] to find out more.

Error messages in PySpark can be especially unhelpful - often returning hundreds of lines of messages for a simple error. We've found it easier to log only the start of these error messages. This snippet of code shows how:

```python
    try:
        df.agg(*aggregate_fields)
    except pyspark.sql.utils.AnalysisException as e:
        logger.error(f"This is a PySpark error. Please check your variable: {str(e).split(';')[0]}")
        sys.exit(1)
```

Just as before we are using the control error handling gives us to log a useful error message. However, in this case the exception encountered is a custom PySpark exception rather than an inbuilt python exception. PySpark exceptions produce a different stack trace which is long and sometimes difficult to read. So not only do we use error handling here to log our error message, we also take this opportunity to log a more informative readable message as well.

[1]: ../python/logging-and-error-handling.md

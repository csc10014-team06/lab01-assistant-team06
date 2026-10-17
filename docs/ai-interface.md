# AI Service Interface (Proposed)

**Status:** Design only — no LLM integration is implemented in Lab 2.

## 1. Purpose

Define a stable interface for a future large language model (LLM) service in the Study Assistant. The current assistant answers questions using the rule-based `reply()` function in `src/assistant/rules.py`. A future LLM integration should not break that existing behavior.

## 2. Proposed Python interface

```python
from typing import Literal, TypedDict

class AIResult(TypedDict):
    answer: str
    source: Literal["llm", "rules"]
    error: str | None

def generate_answer(message: str, context: str | None = None) -> AIResult:
    """Return an answer from the future LLM, or use a rule-based fallback."""
```

This signature is a **contract**, not an implemented function.

## 3. Inputs

| Parameter | Type | Description |
| --- | --- | --- |
| `message` | `str` | The user's question. Leading/trailing whitespace may be removed. An empty question must not be sent to an LLM. |
| `context` | `str \| None` | Optional trusted reference text supplied by a future retrieval component. `None` means no additional context. |

## 4. Output

`generate_answer()` returns an `AIResult` dictionary:

| Field | Type | Description |
| --- | --- | --- |
| `answer` | `str` | The text displayed to the user. It must not be empty. |
| `source` | `"llm" \| "rules"` | Whether the answer came from an LLM or the rule-based fallback. |
| `error` | `str \| None` | A short, non-sensitive error code when fallback was needed; otherwise `None`. |

Example of a future successful LLM response:

```json
{"answer": "The Training Office is in room A.101.", "source": "llm", "error": null}
```

The example above is illustrative, not verified project data.

## 5. Error handling

| Condition | Proposed behavior | Error code |
| --- | --- | --- |
| Empty or whitespace-only message | Do not call the LLM; return the current assistant's input prompt. | `invalid_input` |
| API credentials missing | Use the rule-based fallback. | `not_configured` |
| LLM request times out | Use the rule-based fallback. | `timeout` |
| Provider unavailable or rate-limited | Use the rule-based fallback. | `provider_unavailable` |
| Provider returns an empty or malformed answer | Use the rule-based fallback. | `invalid_response` |

Do not expose API keys, internal prompts, or raw exception details in user-facing answers or logs.

## 6. Fallback behavior

If the LLM is unavailable, is not configured, or produces an invalid response, call the existing `assistant.rules.reply(message)` function and return:

```python
{
    "answer": reply(message),
    "source": "rules",
    "error": "provider_unavailable",  # replace with the actual error code
}
```

This preserves the assistant's existing greetings, office lookups, and safe unknown-question response. For example, an unanswered question should keep the existing rule-based response rather than fabricate an answer.

## 7. Future integration and testing

- Keep the LLM provider behind this interface so callers do not depend on a specific API.
- Do not send secrets or unnecessary personal information to an LLM provider.
- Add unit tests for input validation, response structure, timeout, provider errors, and fallback before implementing an LLM call.
- The current Lab 2 change is documentation only: **no API call, credentials, provider SDK, or runtime code changes**.

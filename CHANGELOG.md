# Changes

## Version 1.2.0
* Avoid adding an xref to the table if tickets are unused in the templates (which caused a broken xref)
* Switch to RN in definition list format, auto-convert RN in old format to definition lists

## Version 1.1.2

* Add clickable URLs for tickets
* Print a better message when ticket was moved
* Log references for tickets that have them
* Fix compilation warning

## Version 1.1.1

* Update jira_query dependency
* Update a log level

## Version 1.1.0

* Acorns can now also be used with the Atlassian Cloud if you set the `JIRA_ATLASSIAN_CLOUD` environment variable to `true`. For compatibility reasons, if the variable does not exist, Acorns continues to use the API calls for an on-premise Jira instance.

## Version 1.0.2

* The subsystem field for Jira can now also handle if a single object is returned from Jira. This is required because the PoolTeam field (array) will be replaced with AssignedTeam (single-value).

## Version 0.32.0

* Enable Team as an alternative Subsystems field structure (RHELDOCS-17810). The field structure is:

    ```
    Team { name: string, id: number }
    ```

## Version 0.31.1

* Fixes and minor improvements to the example configuration files.
* A nicer info message about the switched target releases.

## Version 0.31.0

* More accurately parse and report target releases. If the second most common release in the project is more recent than the first most common, assume that the second release is the active one. [#13](https://github.com/msuchane/acorns/issues/13).

## Version 0.30.2

* Attempt to fix [#23](https://github.com/msuchane/acorns/issues/23).

## Version 0.30.1

* Fix a typo.

## Version 0.30.0

* You can attach a footnote to explain why private ticket IDs contain no links ([#24](https://github.com/msuchane/acorns/issues/24)).

## Version 0.29.0

* Jira tickets can now have clickable links if the ticket is public.
* You can set a Jira project as private to disable links to it.

## Version 0.28.7

* In the status table, list the ticket's resolution next to its status if the ticket is closed.

## Version 0.28.6

* Use the Jira issue key rather than ID in an error message. The ID is a Jira internal code, whereas the key is the human-readable code that we use in release notes.

## Version 0.28.5

* If a Jira doc text status field exists but it empty (`None`), treat it as an In Progress release note and log a warning. Previously, an empty field caused a build failure.
* Update dependencies.

## Version 0.28.4

* Fix a bug caused by an unset ticket priority.
* Update dependencies.

## Version 0.28.3

* Process the doc text status field as case-insensitive.

## Version 0.28.2

* Switch from OpenSSL to RusTLS for better portability.
* Fix the verbose option.

## Version 0.28.1

* Updated dependencies.

## Version 0.28.0

* Disable the footnote for now. It did not render with Pantheon.

* Remove the parentheses around ticket IDs.

## Version 0.27.1

* Use a different footnote attribute, as recommended by the official `asciidoctor` documentation.

  Instead of the `{PrivateFootnote}` attribute containing the footnote text, it is now the `fn-private` attribute that contains the whole footnote macro.

## Version 0.27.0

* Private ticket IDs now feature a footnote that explains why the ID is not clickable. You can override the footnote text using the `{PrivateFootnote}` attribute.

## Version 0.26.1

* The tool now recognizes the legacy `cizrna/` directory path for compatibility with previous releases.

## Version 0.26.0

* Renamed from Cizrna to aCoRNs.

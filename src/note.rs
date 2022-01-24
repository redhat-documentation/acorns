use crate::ticket_abstraction::AbstractTicket;
use bugzilla_query::Bug;
use jira_query::JiraIssue;

pub fn display_bugzilla_bug(bug: &Bug) -> String {
    let abstract_ticket = AbstractTicket::from(bug.clone());
    abstract_ticket.release_note()
}

pub fn display_jira_issue(issue: &JiraIssue) -> String {
    let doc_text = issue
        .fields
        .extra
        .get("customfield_12317322")
        .unwrap()
        .as_str()
        .unwrap()
        .to_string();
    doc_text
}
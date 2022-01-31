use std::fs;
use std::path::Path;

use log::debug;
use serde::Deserialize;

#[derive(Debug, PartialEq, Deserialize)]
pub struct Ticket {
    pub tracker: tracker::Service,
    pub key: String,
}

pub mod tracker {
    use serde::Deserialize;

    #[derive(Debug, PartialEq, Deserialize)]
    pub enum Service {
        Bugzilla,
        Jira,
    }

    #[derive(Debug, PartialEq, Deserialize)]
    pub struct Instance {
        pub host: String,
        pub api_key: String,
    }

    #[derive(Debug, PartialEq, Deserialize)]
    pub struct Config {
        pub jira: Instance,
        pub bugzilla: Instance,
    }
}

pub fn parse(config_file: &Path, trackers_file: &Path) -> (Vec<Ticket>, tracker::Config) {
    let text = fs::read_to_string(config_file).unwrap();
    let config: Vec<Ticket> = serde_yaml::from_str(&text).unwrap();
    debug!("{:#?}", config);

    let text = fs::read_to_string(trackers_file).unwrap();
    let trackers: tracker::Config = serde_yaml::from_str(&text).unwrap();
    debug!("{:#?}", trackers);

    (config, trackers)
}

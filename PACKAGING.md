# Packaging acorns

The following are instructions for the maintainers of `acorns` to package and distribute new releases.


## Preparing a new version

1. Update acorns dependencies:

    ```
    $ cargo update
    ```

2. Make your changes to the code and merge them to the `main` branch.

3. Update the version number in `Cargo.toml` and `acorns.spec`. The versions must be identical.

4. Update `CHANGELOG.md`.

5. Commit the version update:

    ```
    $ git commit -am "Update the version to X.Y.Z"
    ```

6. Tag the latest commit with the new version number:

    ```
    $ git tag -a vX.Y.Z -m "Version X.Y.Z"
    ```

    Make sure to prefix the version in the tag name with "v" for "version".

7. Push the version tag to the remote repository:

    ```
    $ git push --follow-tags
    ```

    If you're using several remote repositories, such as origin and upstream, make sure to push the tag to all of them.


## Packaging and distributing acorns as an RPM package

1. Log into the Copr repository administration.

    Currently, acorns is packaged in the [mmuehlfeldrh/acorns](https://copr.fedorainfracloud.org/coprs/mmuehlfeldrh/acorns/) repository.

2. Go to the **Builds** tab.

3. Click **New Build**.

4. Select **SCM**.

5. In the **Clone url** field, paste `https://github.com/redhat-documentation/acorns`.

6. In the **Spec File** field, use `acorns.spec`.

7. Click **Build**.


## Packaging and distributing acorns with Homebrew

1. Make sure you have access to the existing Homebrew repository.

    Currently, acorns is packaged in [redhat-documentation/homebrew-repo](https://github.com/redhat-documentation/homebrew-repo).

2. Download the `.tar.gz` archive that Github created for your latest tagged version:

    <https://github.com/redhat-documentation/acorns/tags>

3. Calculate the SHA256 checksum of this archive:

    ```
    $ sha256sum vX.Y.Z.tar.gz
    ```

4. In the `homebrew-repo` repository, edit the `Formula/acorns.rb` file.

5. In the `url` attribute, update the version in the URL to your latest version.

6. In the `sha256` attribute, replace the existing checksum with the new checksum that you calculated.

7. Commit and push the changes.


## Packaging and distributing acorns on Quay.io

Currently, acorns is packaged in [redhat-documentation/acorns](https://quay.io/repository/redhat-documentation/acorns).

When you push a tagged version to the [redhat-documentation/acorns](https://github.com/redhat-documentation/acorns) Git repository, it automatically triggers a rebuild of the container. Once the container for the new version is ready, you can assign the `latest` tag to it.

The version tag must start with "v" and match the `v.*` regular expression.

Details on configuring the automatic build trigger: TODO.


## Packaging and distributing acorns on Crates.io

1. If you are publishing to Crates.io for the first time on this system, log into your account:

    ```
    $ cargo login
    ```

    You can manage your login tokens in your account settings: <https://crates.io/me>.

2. Publish the latest version of `acorns` to Crates.io:

    ```
    $ cargo publish
    ```


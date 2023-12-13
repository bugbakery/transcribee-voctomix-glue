let
  # We use a fixed version of nixpkgs here, so we get a recent enough version of
  # pdm (2.4.6 at the time of writing). The version shipped in current (as of 12-03-23)
  # nixpkgs-stable does not support dependencies with relative paths
  pkgs = import
    (fetchTarball {
      name = "nixpkgs-unstable-new-enough-pdm";
      url = "https://github.com/NixOS/nixpkgs/archive/43862987c3cf2554a542c6dd81f5f37435eb1423.tar.gz"; # keep in sync with .github/workflows/lint.yml

    })
    { };
  pdm = pkgs.pdm.overridePythonAttrs (old: rec {
    version = "2.4.9";
    pname = old.pname;
    src = pkgs.fetchPypi {
      inherit pname version;
      sha256 = "28b/sZXzmrJLS8tQf+mXiaYaMhWdi/In8xF7lPMn8vI=";
    };
    doCheck = false;
  });
in
pkgs.mkShell {
  buildInputs = with pkgs; [
    pre-commit

    python310
    python310Packages.black
    pdm

    # required by pre-commit
    git
    ruff
  ];
}
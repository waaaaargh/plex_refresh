{ sources ? import ./nix/sources.nix
, pkgs ? import sources.nixpkgs { }
}:

pkgs.python3Packages.buildPythonApplication {
  pname = "flaskrefresh";
  src = ./.;
  version = "0.1";
  propagatedBuildInputs = [
    pkgs.python3Packages.fire
    pkgs.python3Packages.plexapi
  ];
}

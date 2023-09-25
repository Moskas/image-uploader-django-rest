{
  description = "Python dev flake";

  inputs = { nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable"; };
  outputs = { self, nixpkgs, ... }:
    let
      system = "x86_64-linux";
      pkgs = import nixpkgs {
        inherit system;
        config.allowUnfree = true;
      };
    in {
      devShell.x86_64-linux = pkgs.mkShell {
        buildInputs = with pkgs; [
          python310
          python310Packages.pyls-flake8
          python310Packages.black
          python310Packages.django
          python310Packages.django-rest-registration
          python310Packages.requests
          python310Packages.pillow
          python310Packages.celery
          redis
          sqlite
          postman
        ];
      };
    };
}

import argparse
import logging
from pyecore.ecore import EPackage
from pyecore.resources import ResourceSet, URI  # Correct import
from pyecoregen.ecore import EcoreGenerator

def generate_classes(ecore_path, output_dir):
    # Load Ecore model
    resource_set = ResourceSet()
    resource = resource_set.get_resource(ecore_path)
    root_package = resource.contents[0]  # Get root EPackage

    # Configure generator with auto-registration
    generator = EcoreGenerator(
        auto_register_package=True,
        user_module=None,
        with_dependencies=False
    )

    # Generate Python classes
    generator.generate(root_package, output_dir)
    logging.info(f"Generated classes in {output_dir}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate Python classes from Ecore model')
    parser.add_argument('-e', '--ecore', required=True, help='Path to .ecore file')
    parser.add_argument('-o', '--output', required=True, help='Output directory')
    parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    args = parser.parse_args()

    logging.basicConfig(level=logging.DEBUG if args.verbose else logging.INFO)
    generate_classes(args.ecore, args.output)

def count_panels(floor_width, floor_length, panel_width, panel_length, panels_in_package):
    floor_size = floor_width * floor_length
    floor_size = floor_size * 1.1

    panel_size = panel_width * panel_length
    total_panels = floor_size / panel_size

    required_packages = total_panels / panels_in_package

    if isinstance(required_packages, float):
        required_packages = int(required_packages)
        required_packages = required_packages + 1

    return required_packages


print(count_panels(5, 5, 1, 1, 5))

# 3DViewPy

## Overview

This project is a basic 3D renderer created using mathematical principles. It offers two different viewing modes: **Pythagorean** and **Thales**.

## Basic Usage

To use the renderer, import the module and create a `Renderer` instance with the desired dimensions and view mode. For example:

```python
from renderer.renderer import Renderer, ViewCamera

renderer = Renderer(400, 400, ViewCamera.PYTHAGORE)
renderer.new_mesh([(0, 0, 0), (0, 1, 0), (1, 0, 0)])
renderer.new_mesh([(0, 0, 0), (0, 1, 0), (0, 0, 1)])
renderer.launch()
```

### View Examples

- **Pythagorean view:**

![Pythagorean view](https://res.craft.do/user/full/9158afb0-cf4f-70e7-4f73-e7b4bccede14/doc/4439b81c-461c-47c4-9ac7-34152aefea9e/207069cb-d01c-416e-b573-4d17b3a05765)

- **Thales view:**

![Thales view](https://res.craft.do/user/full/9158afb0-cf4f-70e7-4f73-e7b4bccede14/doc/4439b81c-461c-47c4-9ac7-34152aefea9e/74548607-d593-4081-8c3b-03f7cc50804c)

### Adding New Meshes

Add new meshes with the following function:

```python
renderer.new_mesh([(0, 0, 0), (0, 1, 0), (1, 0, 0)])
```

## Movement and Rotation

Navigate using the WQSD keys or arrow keys. Use the mouse to rotate the camera horizontally.

[Example Video](https://res.craft.do/user/full/9158afb0-cf4f-70e7-4f73-e7b4bccede14/doc/4439b81c-461c-47c4-9ac7-34152aefea9e/2d8a9992-19dc-40f6-8d9b-789f89929a95)

## How It Works
You can have any details in this [doc](https://cocosol.fr/blog/renderer)

### Limitations and Improvements

**Z Buffer:** Currently missing; important for handling depth and occlusion. Future improvements will include adding this feature.

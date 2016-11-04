# elm-scaffold
Very simple module scaffolding tool for Elm written in python 3

This tool generates files for a new Elm module using the structure I generally apply in my project.

Not elegant, not error proof, not pythonic, just get the job done ASAP. :)

## Requirements

* the only requirement is to have python 3 installed
* using os and argparse modules

## Usage


```
usage: scaffold.py [-h] moduleName

Elm module scaffolding tool

positional arguments:
  moduleName  fully qualified name of the module. (for instance,
              "Example.Admin.Blog")

optional arguments:
  -h, --help  show this help message and exit

```

If you supply Example.Admin.Blog as parameter, it will generate the following 3 files:

Example/Admin/Blog/Types.elm:
```elm

module Example.Admin.Blog.Types exposing (..)

type BlogRoute
    = BlogRoute


type BlogMsg
    = BlogMsg


type alias BlogModel =
    { route : BlogRoute }
    
```

Example/Admin/Blog/View.elm:
```elm

module Example.Admin.Blog.View exposing (..)

import Html exposing (Html, div)

import Example.Admin.Blog.Types exposing (..)

view : BlogModel -> Html BlogMsg
view model = div [] []

```

Example/Admin/Blog/Core.elm:

```elm

module Example.Admin.Blog.Core exposing (init, update, urlUpdate, subscriptions)

import Example.Admin.Blog.Types exposing(..)

init : BlogRoute -> ( BlogModel, Cmd BlogMsg )
init route =
    ( { route = BlogRoute }, Cmd.none)

update : BlogMsg -> BlogModel -> ( BlogModel, Cmd BlogMsg )
update msg model =
    (model, Cmd.none)

urlUpdate : BlogRoute -> BlogModel -> ( BlogModel, Cmd BlogMsg )
urlUpdate route model = ( model, Cmd.none )

subscriptions : BlogModel -> Sub BlogMsg
subscriptions state =
    Sub.none

```

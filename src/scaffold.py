import argparse
import os

typesTemplate = """module {fullModule}.Types exposing (..)

type {module}Route
    = {module}Route


type {module}Msg
    = {module}Msg


type alias {module}Model =
    {{ route : {module}Route }}"""

viewTemplate = """module {fullModule}.View exposing (..)

import Html exposing (Html, div)

import {fullModule}.Types exposing (..)

view : {module}Model -> Html {module}Msg
view model = div [] []
"""

coreTemplate = """module {fullModule}.Core exposing (..)

import {fullModule}.Types exposing(..)

init : {module}Route -> ( {module}Model, Cmd {module}Msg )
init route =
    ( {{ route = BlogRoute }}, Cmd.none)

update : {module}Msg -> {module}Model -> ( {module}Model, Cmd {module}Msg )
update msg model =
    (model, Cmd.none)

urlUpdate : {module}Route -> {module}Model -> ( {module}Model, Cmd {module}Msg )
urlUpdate route model = ( model, Cmd.none )

subscriptions : {module}Model -> Sub {module}Msg
subscriptions state =
    Sub.none
"""

def parseArgs():
    parser = argparse.ArgumentParser(description='Elm module scaffolding tool')
    parser.add_argument('moduleName', help='full name of the module. ("Elm.Main.App")')
    return parser.parse_args()

if __name__ == "__main__":
    args = parseArgs()
    parts = args.moduleName.split('.')
    folderHierarchy = parts

    moduleName = parts[-1]
    os.makedirs(os.path.join(*folderHierarchy), exist_ok=True)

    f = open(os.path.join(*parts, 'Types.elm'), 'wt', encoding='utf-8')
    f.write(typesTemplate.format(fullModule=(args.moduleName), module=moduleName))
    f.close()

    f = open(os.path.join(*parts, 'View.elm'), 'wt', encoding='utf-8')
    f.write(viewTemplate.format(fullModule=(args.moduleName), module=moduleName))
    f.close()

    f = open(os.path.join(*parts, 'Core.elm'), 'wt', encoding='utf-8')
    f.write(coreTemplate.format(fullModule=(args.moduleName), module=moduleName))
    f.close()

    print("haho")


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

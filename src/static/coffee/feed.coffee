class Site
  constructor: (@el) ->
    @id = @el.find('input[type=checkbox]')[0].id.substr 1

  subscribe: =>
    $.post '/feed', id: @id

  unsubscribe: =>
    $.ajax
      url: '/feed'
      method: 'DELETE'
      data: id: @id

  getText: =>
    return @el.text().toLowerCase()

  showOrHide: (text) =>
    if @getText().indexOf(text) > 0
      @el.removeClass 'hidden'
      return

    @el.addClass 'hidden'


class Feed
  constructor: (@el) ->
    @el.find 'input[type=checkbox]'
      .change ->
        site = new Site $(this).parent('li')
        if this.checked then site.subscribe() else site.unsubscribe()

    @el.find 'input[type=search]'
      .keyup (e) => @search e.target.value.toLowerCase()

  search: (text) =>
    elements = @el.find('li')
    if !text.length
      elements.removeClass 'hidden'
      return

    elements.each (i, item) ->
      new Site($(item)).showOrHide text

new Feed $('section')

class AjaxSearch {
    constructor(container) {
        if(container.find('#search').length > 0) {
            this.searchBar = container.find('#search');
        } else {
            this.searchBar = $("<input id=\"search\" class=\"form-control\" type=\"search\" placeholder=\"Search\" aria-label=\"Search\">");
            container.append(this.searchBar);
        }

        if(container.find('#results').length > 0) {
            this.resultContainer = container.find('#results');
        } else {
            this.resultContainer = $("<div class=\"dropdown-menu\" id=\"results\"></div>");
            container.append(this.resultContainer);
        }
        this.resultContainer.css('width', '100%');

        this.focusedIndex = -1;
        this.resultLength = -1;
        this.resultElements = [];
        this.container = container;
        this.bindEvents();
    }

    bindEvents() {
        var self = this;
        this.searchBar.on('keyup', function(e) {
            if (e.which == 37 || e.which == 39 || e.which == 38 || e.which == 40) {
                return;
            } else if(e.which == 13 && this.focusedIndex != -1) {
                self.goToFocusedText();
                return;
            }

            var filtro = self.searchBar.val();
            if(filtro.length > 2) {
                $.ajax({
                    url: "/AnalizzaVocabolario/search",
                    type: "GET",
                    data: {'filtro': filtro},
                    dataType: "json",
                    beforeSend: function() {
                        self.setSearching();
                        self.container.addClass('open');
                    },
                    success: function (data) {
                        if(data['status'] == false) {
                            self.setNoResult()
                        } else {
                            self.setResultsList(data);
                        }
                    },
                    error: function (jqXHR, textStatus) {
                        console.log(jqXHR);
                        alert("Something went wrong with your search");
                    }
                });
            } else {
                self.container.removeClass('open');
            }
        });

        this.searchBar.on('keydown', function(e) {
            if(e.which == 40) { // down arrow
                self.incrementFocus();
            } else if (e.which == 38) { // up arrow
                self.decrementFocus();
            }
        });
    }

    setResultsList(data) { 
        var self = this;
        data = JSON.parse(data)

        self.emptyResults();
        self.resultLength = data.length;

        $.each(data, function(i, item) {
            var link_to_item = '/AnalizzaVocabolario/features/' + item.pk;
            var item_title = item.fields.titolo;
            var element = $("<a class=\"dropdown-item\" href=\"" + link_to_item + "\">" + item_title + "</a>")
            self.resultElements.push(element);
            self.resultContainer.append(element);
        });
    }

    setSearching() {
        this.emptyResults();
        this.resultContainer.append("<a><span style='margin-left: 20px'>Searching ...</span></a>")
    }

    setNoResult() {
        this.emptyResults();
        this.resultContainer.append("<a><span style='margin-left: 20px'>No result</span></a>")
    }

    emptyResults() {
        this.resultContainer.empty();
        this.resultElements = [];
        this.focusedIndex = -1;
        this.resultLength = 0;
    }

    incrementFocus() {
        console.log(this.resultLength);
        if(this.focusedIndex >= (this.resultLength - 1)) return;
        this.focusedIndex++;
        this.refreshFocus();
    }

    decrementFocus() {
        if(this.focusedIndex <= -1) return; 
        this.focusedIndex--;
        this.refreshFocus();
    }

    refreshFocus() {
        for(var i = 0; i < this.resultElements.length; i++) {
            this.resultElements[i].css('background', 'white');
        }

        if(this.focusedIndex == -1) {
            return
        } else {
            this.resultElements[this.focusedIndex].css('background', 'antiquewhite');
        }
    }

    goToFocusedText() {
        window.location = this.resultElements[this.focusedIndex].attr('href');
    }
}
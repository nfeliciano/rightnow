var rightnow = angular.module('rightnow', ['ui.router']);

rightnow.config(function($stateProvider, $urlRouterProvider) {
  $urlRouterProvider.otherwise("/form/1");
  $stateProvider
    .state('form', {
      url: '/form',
      templateUrl: '/static/partials/form.html',
      controller: 'formController'
    })
    .state('form.when', {
      url: '/1',
      templateUrl: '/static/partials/form-when.html'
    })
    .state('form.what', {
      url: '/2',
      templateUrl: '/static/partials/form-what.html'
    });
});

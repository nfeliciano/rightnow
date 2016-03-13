var rightnow = angular.module('rightnow', ['ui.router']);

rightnow.config(function($stateProvider, $urlRouterProvider) {
  $urlRouterProvider.otherwise("/form/time");
  $stateProvider
    .state('form', {
      url: '/form',
      templateUrl: '/static/partials/form.html',
      controller: 'formController'
    })
    .state('form.time', {
      url: '/time',
      templateUrl: '/static/partials/form-time.html'
    })
    .state('form.what', {
      url: '/what',
      templateUrl: '/static/partials/form-what.html'
    });
});

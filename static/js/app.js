var rightnow = angular.module('rightnow', ['ngAnimate','ui.router', 'ngTouch']);

rightnow.config(function($stateProvider, $urlRouterProvider) {
  $urlRouterProvider.otherwise("/form/what");
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
    })
    .state('form.activity', {
      url: '/activity',
      templateUrl: '/static/partials/form-activity.html'
    })
    .state('form.event', {
      url: '/event',
      templateUrl: '/static/partials/form-event.html'
    })
    .state('form.event2', {
      url: '/event2',
      templateUrl: '/static/partials/form-event.html'
    });
});

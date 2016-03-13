rightnow.controller('formController', function($rootScope, $scope, $state, $http) {
  $scope.formData = {};
  $scope.selectedTime = { name: 'None' };
  $scope.selectedEventType = { name: 'None' };
  $scope.atEvent = false;
  $scope.atStart = true;

  $rootScope.$on('$viewContentLoading',
    function(event, viewConfig){
      if ($state.$current == 'form.event' || $state.$current == 'form.event2') {
        if ($.isEmptyObject($scope.formData)) {
          $state.transitionTo('form.what');
        }
      }
  });

  $scope.tryText = [
    { type: 'normal',
      quote: 'You should check out' },
    { type: 'normal',
      quote: 'A friend told me about' },
    { type: 'normal',
      quote: 'Uhhhhhhhh... Try' },
    { type: 'normal',
      quote: 'Take a look at' },
    { type: 'question',
      quote: 'Maybe' },
    { type: 'question',
      quote: 'Have you heard about' },
    { type: 'question',
      quote: 'You wanna go to' },
    { type: 'question',
      quote: 'Have you ever tried' },
    { type: 'exclamation',
      quote: 'Duh! Go to' },
    { type: 'exclamation',
      quote: 'You haven\'t lived until you\'ve been to' },
    { type: 'exclamation',
      quote: 'I\'ve decided. We\'re going to' },
    { type: 'exclamation',
      quote: 'You know what? Let\'s do' }
  ];

  $scope.times = [
    { name: 'Right Now!' },
    { name: 'Later Tonight' },
    { name: 'Tomorrow' },
    { name: 'This Friday' },
    { name: 'This Saturday' }
  ];

  $scope.eventTypes = [
    { name: 'Something to eat' },
    { name: 'Somewhere to hang out' },
    { name: 'Something happening right now' }
  ];

  $scope.activityTypes = [
    { name: 'Yes!' }, //outdoors
    { name: 'Nope' } //indoors
  ];

  $scope.timeSelected = function() {
    //change here
    $state.transitionTo('form.what');
  }

  $scope.eventTypeSelected = function() {
    //change here
    $scope.atStart = false;
    if ($scope.formData.eventType.name == 'Something to eat' || $scope.formData.eventType.name == 'Something happening right now')
      $scope.sendQuery();
    else {
      // $scope.activityTypeSelected();
      $state.transitionTo('form.activity');
    }
  }

  $scope.activityTypeSelected = function() {
    //change here
    // $scope.eventTypeSelected();
    $scope.formData.eventType.name = 'Somewhere to hang out';
    $scope.sendQuery();
  }

  $scope.sendQuery = function() {
    //change here
    $http.get(getQueryString($scope.formData))
    .success(function(data) {
      $scope.meetJason = data.result[0];
      if ($scope.atEvent == false) {
        $state.transitionTo('form.event');
      } else {
        if ($state.$current == 'form.event') {
          $state.transitionTo('form.event2');
        } else if ($state.$current == 'form.event2') {
          $state.transitionTo('form.event');
        }
      }
      $scope.randomText = $scope.tryText[Math.floor(Math.random() * $scope.tryText.length)];
      $scope.atEvent = true;
    }).error(function(error) {
      console.log(error);
    });
  }

  $scope.startOver = function() {
    $scope.atEvent = false;
    $scope.atStart = true;
    $state.transitionTo('form.what');
  }

  function getQueryString(formData) {
    if (formData.eventType.name == 'Something to eat') {
      $scope.selectedEventType.name = 'icon-spoon-knife';
      return 'api?random=10&table=restaurants';
    } else if (formData.eventType.name == 'Somewhere to hang out') {
      $scope.selectedEventType.name = 'icon-dice';
      return 'api?random=10&table=activities';
    } else {
      $scope.selectedEventType.name = 'icon-calendar';
      return 'api?random=1&table=events';
    }
  }

  $scope.swipeLeft = function() {
    if ($state.$current == 'form.event' || $state.$current == 'form.event2') {
      $scope.sendQuery();
    }
  }
});

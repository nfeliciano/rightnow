rightnow.controller('formController', function($scope, $state, $http) {
  $scope.formData = {};
  $scope.selectedTime = { name: 'None' };
  $scope.selectedEventType = { name: 'None' };
  $scope.atEvent = false;
  $scope.atStart = true;

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
    if (formData.eventType.name == 'Something to eat')
      return 'api?random=10&table=restaurants';
    else if (formData.eventType.name == 'Somewhere to hang out')
      return 'api?random=10&table=activities';
    else return 'api?random=1&table=events';
  }

  $scope.swipeLeft = function() {
    if ($state.$current == 'form.event' || $state.$current == 'form.event2') {
      $scope.sendQuery();
    }
  }
});

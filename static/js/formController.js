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
    { name: 'Restaurant' },
    { name: 'Activity' },
    { name: 'Event' }
  ];

  $scope.activityTypes = [
    { name: 'Outdoor Activities' },
    { name: 'Nightlife Activities' }
  ];

  $scope.timeSelected = function() {
    //change here
    $state.transitionTo('form.what');
  }

  $scope.eventTypeSelected = function() {
    //change here
    $scope.atStart = false;
    if ($scope.formData.eventType.name == 'Restaurant' || $scope.formData.eventType.name == 'Event')
      $scope.sendQuery();
    else {
      // $scope.activityTypeSelected();
      $state.transitionTo('form.activity');
    }
  }

  $scope.activityTypeSelected = function() {
    //change here
    // $scope.eventTypeSelected();
    $scope.formData.eventType.name = 'Activity';
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
    if (formData.eventType.name == 'Restaurant')
      return 'api?random=10&table=restaurants';
    else if (formData.eventType.name == 'Activity')
      return 'api?random=10&table=activities';
    else return 'api?random=1&table=events';
  }

  $scope.swipeLeft = function() {
    if ($state.$current == 'form.event' || $state.$current == 'form.event2') {
      $scope.sendQuery();
    }
  }
});

rightnow.controller('formController', function($scope, $state, $http) {
  $scope.formData = {};
  $scope.selectedTime = { name: 'None' };
  $scope.selectedEventType = { name: 'None' };

  $scope.times = [
    { name: 'Right Now!' },
    { name: 'Later Tonight' },
    { name: 'Tomorrow' },
    { name: 'This Friday' },
    { name: 'This Saturday' }
  ];

  $scope.eventTypes = [
    { name: 'A' },
    { name: 'B' },
    { name: 'C' },
    { name: 'D' },
    { name: 'E' }
  ];

  $scope.findEvent = function() {
    alert('FIND SOMETHING');
  }

  $scope.timeSelected = function() {
    //change here
    $state.transitionTo('form.what');
  }

  $scope.eventTypeSelected = function() {
    //change here
    $state.transitionTo('form.what');
  }

  // $scope.meetJason = {
  //   id: '11',
  //   name: 'Itami Sushi',
  //   address: '615 Yates St',
  //   description: 'Excellent food and friendly service makes your dining experience a pleasure. Azuma Sushi, a newly opened and renovated Japanese restaurant located in the heart of downtown Victoria. Ingredients are hand-picked fresh daily. Sushi are made right when you order. We offer a variety of food from convenient Bento Boxes, Lunch and Dinner Combos and Sushi dishes. All items in the menu may be take out in a special bento box, complete with chopsticks and soy sauce.',
  //   url: 'http://www.tourismvictoria.com/includes/redirects/webcount.cfm?listingID=33959'
  // };

  $http.get('api?random=1&table=activities')
    .success(function(data) {
      $scope.meetJason = data.result[0];
    }).error(function(error) {
      console.log(error);
    });
});

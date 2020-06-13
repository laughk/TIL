angular.module('myApp', [])
  .controller('MyController', ['$scope', function($scope) {
    // [上位に通知] ボタンのクリックで上位スコープに通知
    $scope.onemit = function() {
      $scope.$emit('notify', 'Emit');
    };

    // [下位に通知] ボタンのクリックで下位スコープに通知
    $scope.onbroad = function() {  
      $scope.$broadcast('notify', 'Broadcast', new Date());
    };
  }])
  .controller('ParentController', ['$scope', function($scope) {
    $scope.$on('notify', function(e, date){
      $scope.parentResult = e.name + '/' + e.targetScope.message + '/' + date;
    });
  }])
  .controller('Child1Controller', ['$scope', function($scope) {
    $scope.$on('notify', function(e, date, current){
      $scope.child1Result = e.name + '/' + e.targetScope.message
        + '/' + date + '/' + current.toLocaleString();
    });
  }])
  .controller('Child2Controller', ['$scope', function($scope) {
    $scope.$on('notify', function(e, date, current){
      $scope.child2Result = e.name + '/' + e.targetScope.message
        + '/' + date + '/' + current.toLocaleString();
    });
  }]);
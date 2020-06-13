angular.module('myApp', [])
    .controller('ParentController', ['$scope', function($scope) {
        $scope.value = 1;

        $scope.onparent = function() {
            $scope.value++;
        };
    }])
    .controller('ChildController', ['$scope', function($scope) {
        $scope.onchild = function() {
            $scope.$parent.value++;
        }
    }]);
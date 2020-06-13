angular.module('myApp', [])
    .controller('MyController', function($scope, BookList) {
        $scope.books = BookList();
    })
    .value('BookList', function(){
        return [
            {
                isbn: '978-4-7741-7078-7',
                title: 'サーブレット&JSPポケットリファレンス',
                price: 2680,
                publish: '技術評論社',
                published: new Date(2015, 0, 8)
            },
            {
                isbn: '978-4-7741-6127-3',
                title: 'iPhone/iPad開発ポケットリファレンス',
                price: 2780,
                publish: '技術評論社',
                published: new Date(2013, 10, 23)
            }
        ];
    });
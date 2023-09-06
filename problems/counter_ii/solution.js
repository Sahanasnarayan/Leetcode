var createCounter = function(init) {
    var res= init;
    return {
        increment (){
            return ++init;
        },
        decrement (){
            return --init;
        },
        reset(){
            return init = res;
        }
    }
};
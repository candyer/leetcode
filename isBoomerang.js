// https://leetcode.com/problems/valid-boomerang/description/

// 1037. Valid Boomerang

// A boomerang is a set of 3 points that are all distinct and not in a straight line.

// Given a list of three points in the plane, return whether these points are a boomerang.

// Example 1:
// Input: [[1,1],[2,3],[3,2]]
// Output: true

// Example 2:
// Input: [[1,1],[2,2],[3,3]]
// Output: false
 

// Note:
// points.length == 3
// points[i].length == 2
// 0 <= points[i][j] <= 100


function isIdentical(point1, point2) {
    return point1[0] === point2[0] && point1[1] === point2[1]
}

var isBoomerang = function(points) {
    if (isIdentical(points[0], points[1]) || isIdentical(points[0], points[2]) || isIdentical(points[1], points[2])){
        return false
    }
    
    let differ = new Set()
    let xs = new Set()
    let ys = new Set()
    for (let i in points) {
        differ.add(points[i][0] - points[i][1])
        xs.add(points[i][0])
        ys.add(points[i][1])
    }
    return differ.size > 1 && xs.size > 1 && ys.size > 1

};

console.log(isBoomerang([[0,0],[2,1],[2,1]]) === false)
console.log(isBoomerang([[1,1],[2,3],[3,2]]) === true)
console.log(isBoomerang([[1,1],[1,1],[3,2]]) === false)
console.log(isBoomerang([[1,1],[2,2],[3,3]]) === false)
console.log(isBoomerang([[1,5],[2,6],[3,7]]) === false)
console.log(isBoomerang([[0,1],[1,1],[2,1]]) === false)
console.log(isBoomerang([[2,1],[2,9],[2,12]]) === false)
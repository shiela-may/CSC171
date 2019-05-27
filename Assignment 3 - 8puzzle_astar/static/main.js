
let tiles = ['t0', 't1', 't2', 't3', 't4', 't5', 't6', 't7', 't8'];
let m = [];

function start(initial, moves) {
    console.log(initial);
    console.log(moves);
    var i;
    for (i = 0; i < tiles.length; i++) {
        var tile_id = "t" + i.toString();
        console.log(tile_id);
        if (initial[i] != '0') {
            var tile = document.getElementById(tile_id);
            tile.classList.remove('blank');
            tile.firstChild.data = initial[i];
        }
        else {
            var tile = document.getElementById(tile_id);
            tile.classList.add('blank');
            tile.firstChild.data = " ";
        }
    }
    for (i = 0; i < moves.length; i++) {
        m.push(moves[i]);
    }
    console.log("SOLVE");
    t = setInterval(function() {move();}, 500);
    if (m.length == 0) {
        clearInterval(t);
    }
}

function get_blank() {
    for (i = 0; i < tiles.length; i++) {
        if (document.getElementById(tiles[i]).firstChild.data == " ") {
            return (tiles[i]);
        }
    }
}

function swap(blank_id, tile_id) {
    tile_id = "t" + tile_id.toString();
    console.log(tile_id);
    var tile = document.getElementById(tile_id);
    var blank = document.getElementById(blank_id);
    blank.firstChild.data = tile.firstChild.data;
    blank.classList.remove('blank');
    tile.firstChild.data = " ";
    tile.classList.add('blank');
}

function solve() {
    // var i;
    // for (i = 0; i < 5; i++) {
        var pos = get_blank();
        console.log(pos.charAt(1));
        console.log(m[0]);
        var pos_int = parseInt(pos.charAt(1));
        if (m[0] == 'up') {
            pos_int = pos_int - 3;
            swap(pos, pos_int);
        }
        else if (m[0] == 'down') {
            pos_int = pos_int + 3;
            swap(pos, pos_int);
        }
        else if (m[0] == 'left') {
            pos_int = pos_int - 1;
            swap(pos, pos_int);
        }
        else {
            pos_int = pos_int + 1;
            swap(pos, pos_int);
        }
    // }
}

function move() {
    if (m.length > 0) {
        solve(m);
        m.shift();
    }
}

function sleep(milliseconds) {
  var start = new Date().getTime();
  for (var i = 0; i < 1e7; i++) {
    if ((new Date().getTime() - start) > milliseconds){
      break;
    }
  }
}
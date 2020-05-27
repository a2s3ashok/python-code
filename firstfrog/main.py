'''
n1 = input('enter first number ')
n2 = input('enter secoend number ')
print('your number is',int(n1)+int(n2))
'''

'''
print(len('ashok go on'[0:5:2]))
'''
'''
mystr = 'ashok go on'
print(mystr.count('o'))'''


a = {'ashok':'solder','pawan':'brother','amar':'big brother'}
for item in a :
    print(item,)
'''
a['aman'] = 'chicken'
#print(a['amar'])#only one key can use in it
a['babloo'] = 'goat'
del a['aman']
print(a)
'''
let w = 500;
let h = 500;
let riverArr = [];
let distanceArr = [];

function setup() {
    createCanvas(w, h);
}

function draw() {
    background(240);
    generatePoints();

    for (i = 1; i < riverArr.length; i++) {
        let x1 = parseInt(riverArr[i][0]);
        let y1 = parseInt(riverArr[i][1]);

        let x2 = parseInt(riverArr[i - 1][0]);
        let y2 = parseInt(riverArr[i - 1][1]);

        line(x1, y1, x2, y2);

        let d = int(dist(x1, y1, x2, y2));

        ellipse(x1, y1, 5);

        for (j = 0; j <= x1; j++) {
            for (k = 0; k <= y1; k++){
                rect(j, k, 1);
            }
        }
        distanceArr.push(d);
    }
    noLoop();
}

function generatePoints() {
    let finished;
    riverArr.push([0, random(h)]);
    for (i = 0; i < 4; i++) {
        finished == false;
        riverArr.push([random(w), random(h)]);
        if (i > 0 && riverArr[i][0] <= riverArr[i - 1][0]) {
            console.log(riverArr[i][0], riverArr[i - 1][0]);
            console.log('Bad path');
        }
        finished == true;
    }
    riverArr.push([w, random(h)]);
}

// Test Game

// Initialize Phaser game configuration
var config = {
    type: Phaser.AUTO,
    width: window.innerWidth * 0.7, // Adjusts to the iframe width (assuming the iframe takes up 70% of the page width)
    height: window.innerHeight - 150, // Adjusts to the iframe height (accounting for some padding or margins)
    scene: {
        preload: preload,
        create: create,
        update: update
    }
};

// Create a new Phaser game instance
var game = new Phaser.Game(config);

function preload() {
    // Preload any assets here if needed
}

var square;
var cursors

function create() {
    // Create a simple square
    square = this.add.rectangle(config.width / 2, config.height / 2, 100, 100, 0xff0000);
    square.setOrigin(0.5, 0.5);

    // Enable input events on the square
    square.setInteractive();
    
    // Change color on click
    square.on('pointerdown', function () {
        var randomColor = Math.floor(Math.random() * 16777215).toString(16);
        square.setFillStyle('0x' + randomColor);
    });

    // Set up keyboard input
    cursors = this.input.keyboard.createCursorKeys();
}

function update() {
    // Move the square based on cursor input
    if (cursors.left.isDown) {
        square.x -= 5;
    }
    if (cursors.right.isDown) {
        square.x += 5;
    }
    if (cursors.up.isDown) {
        square.y -= 5;
    }
    if (cursors.down.isDown) {
        square.y += 5;
    }
}

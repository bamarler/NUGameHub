var config = {
    type: Phaser.AUTO,
    width: '100%',
    height: '100%',
    scale: {
        mode: Phaser.Scale.FIT,
        autoCenter: Phaser.Scale.CENTER_BOTH,
    },
    backgroundColor: '#ffffff',
    scene: {
        create: create,
        update: update
    }
};

var game = new Phaser.Game(config);

function create() {
    this.graphics = this.add.graphics();

    // Draw a rectangle
    this.rect = this.add.rectangle(200, 175, 200, 150, 0xff0000);

    // Draw a circle
    this.circle = this.add.circle(400, 300, 100, 0x00ff00);

    // Draw a line
    this.line = this.add.line(0, 0, 600, 100, 600, 500, 0x0000ff, 1.0).setLineWidth(5);

    // Add keyboard input
    this.cursors = this.input.keyboard.createCursorKeys();
    this.keys = this.input.keyboard.addKeys('W,A,S,D');

    // Add mouse input
    this.input.on('pointerdown', function (pointer) {
        this.circle.setFillStyle(Phaser.Display.Color.RandomRGB().color);
    }, this);
}

function update() {
    // Rectangle movement with WASD
    if (this.keys.W.isDown) {
        this.rect.y -= 5;
    }
    if (this.keys.S.isDown) {
        this.rect.y += 5;
    }
    if (this.keys.A.isDown) {
        this.rect.x -= 5;
    }
    if (this.keys.D.isDown) {
        this.rect.x += 5;
    }

    // Circle movement with arrow keys
    if (this.cursors.up.isDown) {
        this.circle.y -= 5;
    }
    if (this.cursors.down.isDown) {
        this.circle.y += 5;
    }
    if (this.cursors.left.isDown) {
        this.circle.x -= 5;
    }
    if (this.cursors.right.isDown) {
        this.circle.x += 5;
    }
}

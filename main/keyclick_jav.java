import javax.sound.sampled.*;
import java.awt.event.*;
import java.io.File;
import java.util.HashMap;
import java.util.Random;
import javax.swing.*;

public class KeySoundPlayer {

    // List of sound files
    private static final String[] soundFiles = {
        "keyboard_click_1.wav",
        "keyboard_click_2.wav",
        "keyboard_click_3.wav",
        "keyboard_click_4.wav",
        "keyboard_click_5.wav"
    };

    // Dictionary to store the last sound played for each key
    private static HashMap<Character, Clip> lastSoundPlayed = new HashMap<>();
    private static Random random = new Random();

    public static void main(String[] args) {
        // Create a frame to listen for key events
        JFrame frame = new JFrame("Key Sound Player");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 400);
        frame.setVisible(true);

        // Add key listener
        frame.addKeyListener(new KeyAdapter() {
            @Override
            public void keyPressed(KeyEvent e) {
                char keyChar = e.getKeyChar();
                System.out.println("Key " + keyChar + " pressed.");

                Clip clip;

                // Check if the sound for this key has already been played
                if (lastSoundPlayed.containsKey(keyChar)) {
                    clip = lastSoundPlayed.get(keyChar); // Use the previously played sound
                } else {
                    // Randomly select a sound file
                    int randomIndex = random.nextInt(soundFiles.length);
                    clip = loadSound(soundFiles[randomIndex]);
                    lastSoundPlayed.put(keyChar, clip); // Store it for future presses
                }

                // Play the sound in a new thread
                new Thread(() -> {
                    if (clip != null) {
                        clip.setFramePosition(0); // Rewind to the beginning
                        clip.start();
                    }
                }).start();
            }

            @Override
            public void keyReleased(KeyEvent e) {
                // Optionally handle key release if needed
                if (e.getKeyCode() == KeyEvent.VK_ESCAPE) {
                    System.exit(0); // Exit on ESC key
                }
            }
        });
    }

    private static Clip loadSound(String filePath) {
        Clip clip = null;
        try {
            File soundFile = new File(filePath);
            AudioInputStream audioInputStream = AudioSystem.getAudioInputStream(soundFile);
            clip = AudioSystem.getClip();
            clip.open(audioInputStream);
        } catch (Exception e) {
            e.printStackTrace();
        }
        return clip;
    }
}

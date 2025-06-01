using UnityEngine;
using UnityEngine.UI;
using UnityEngine.SceneManagement;

public class MainMenu : MonoBehaviour
{
    [Header("Panels")]
    public GameObject mainMenuPanel;
    public GameObject settingsPanel;

    [Header("Audio")]
    public Slider volumeSlider;
    public AudioSource bgmPlayer;

    void Start()
    {
        // Set nilai awal volume dari PlayerPrefs (default 1)
        float savedVolume = PlayerPrefs.GetFloat("BGMVolume", 1f);
        volumeSlider.value = savedVolume;

        if (bgmPlayer != null)
        {
            bgmPlayer.volume = savedVolume;
        }

        // Tambahkan listener saat slider digeser
        volumeSlider.onValueChanged.AddListener(AdjustVolume);
    }

    public void PlayGame()
    {
        SceneManager.LoadScene(SceneManager.GetActiveScene().buildIndex + 1);
    }

    public void ShowSettings()
    {
        mainMenuPanel.SetActive(false);
        settingsPanel.SetActive(true);
    }

    public void ShowMainMenu()
    {
        settingsPanel.SetActive(false);
        mainMenuPanel.SetActive(true);
    }

    public void QuitGame()
    {
        Application.Quit();
        Debug.Log("Game Quit");
    }

    public void AdjustVolume(float value)
    {
        if (bgmPlayer != null)
        {
            bgmPlayer.volume = value;
        }

        PlayerPrefs.SetFloat("BGMVolume", value);
    }
}

using UnityEngine;
using UnityEngine.SceneManagement;

public class PauseMenu : MonoBehaviour
{
    public GameObject pausePanel;
    public GameObject overlay;

    private bool isPaused = false;

    void Update()
    {
        // Toggle pause saat tekan Escape
        if (Input.GetKeyDown(KeyCode.Escape))
        {
            if (isPaused)
            {
                Continue();
            }
            else
            {
                Pause();
            }
        }
    }

    public void Pause()
    {
        if (pausePanel != null)
            pausePanel.SetActive(true);

        if (overlay != null)
            overlay.SetActive(true);

        Time.timeScale = 0f;
        isPaused = true;
    }

    public void Continue()
    {
        if (pausePanel != null)
            pausePanel.SetActive(false);

        if (overlay != null)
            overlay.SetActive(false);

        Time.timeScale = 1f;
        isPaused = false;
    }

    public void Exit()
    {
        Time.timeScale = 1f; // pastikan tidak freeze
        SceneManager.LoadScene("MainMenu");
    }
}

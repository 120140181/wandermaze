using UnityEngine;

public class BackgroundMusic : MonoBehaviour
{
    public static BackgroundMusic Instance;

    private void Awake()
    {
        if (Instance != null && Instance != this)
        {
            Destroy(gameObject); // Hindari duplikat saat scene pindah
            return;
        }

        Instance = this;
        DontDestroyOnLoad(gameObject); // Tetap hidup antar scene
    }
}
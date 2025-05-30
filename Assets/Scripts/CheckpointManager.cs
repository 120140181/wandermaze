using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CheckpointManager : MonoBehaviour
{
    public static CheckpointManager Instance;
    public Vector2? lastCheckpointPosition = null;

    private void Awake()
    {
        if (Instance == null)
        {
            Instance = this;
            DontDestroyOnLoad(gameObject);
        }
        else
        {
            Destroy(gameObject);
        }
    }

    public void SetCheckpoint(Vector2 position)
    {
        lastCheckpointPosition = position;
    }

    public void ResetCheckpoint()
    {
        lastCheckpointPosition = null;
    }
}

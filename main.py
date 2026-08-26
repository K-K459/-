import time

count = 0
max_minutes = 5  # テスト用に5分間（5回）実行して自動終了する設定

print(f"=== カウントアップ処理を開始します（最大 {max_minutes} 分間） ===")

for i in range(1, max_minutes + 1):
    # 1分（60秒）待機
    time.sleep(60)
    count += 1
    print(f"[{i}分経過] 現在のカウント: {count}")

print(f"=== 処理が完了しました。最終カウント: {count} ===")